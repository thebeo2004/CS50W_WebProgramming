document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  document.querySelector('#emails-view').innerHTML = '';

  // Show the mailbox name
  // document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    emails.forEach(email => {
      const emailDiv = document.createElement('div');
      emailDiv.className = 'email';
      emailDiv.innerHTML = `
        <span class="email-sender">${email.sender}</span>
        <span class="email-subject">${email.subject}</span>
        <span class="email-timestamp">${email.timestamp}</span>
      `;

      emailDiv.addEventListener('click', () => load_email(email.id, mailbox, email.archived));

      document.querySelector('#emails-view').appendChild(emailDiv);
    });
  }
  )
}

function load_email(email_id, mailbox, is_archived) {

  document.querySelector('#emails-view').innerHTML = ''

  fetch(`/emails/${email_id}`)
  .then(response => response.json())
  .then(email => {
    const emailDiv = document.createElement('div');
    const userEmail = document.getElementById('emails-view').dataset.useremail;
    emailDiv.className = 'email_view';
    emailDiv.innerHTML = `
      <div><strong>From:</strong> ${email.sender}</div>
      <div><strong>To:</strong> ${userEmail}</div>
      <div><strong>Subject:</strong> ${email.subject}</div>
      <div><strong>Timestamp:</strong> ${email.timestamp}</div>
      <div class="button-group">
        <button class="reply-btn">Reply</button>
        <button class="archive-btn">Archive</button>
      </div>
      <hr>
      <div><p>${email.body}</p></div>
    `;

    document.querySelector('#emails-view').appendChild(emailDiv);

    let archiveBtn = document.querySelector('.archive-btn');

    if (mailbox === 'sent' || mailbox === 'inbox') {
      archiveBtn.textContent = 'Archive';

      document.querySelector('.archive-btn').addEventListener('click', () => {
        fetch(`/emails/${email_id}`, {
          method: 'PUT',
          body: JSON.stringify({
            archived: true
          })
        })
        .then(() => load_mailbox('inbox'))
      })

      if (is_archived) {
        archiveBtn.style.display = 'none';
      }
    } else if (mailbox === 'archive') {
      archiveBtn.textContent = 'Unarchive';

      document.querySelector('.archive-btn').addEventListener('click', () => {
        fetch(`/emails/${email_id}`, {
          method: 'PUT',
          body: JSON.stringify({
            archived: false
          })
        })
        .then(() => load_mailbox('archive'))
      })
    }


  })

  fetch(`/emails/${email_id}`, {
    method: 'PUT',
    body: JSON.stringify({
      read: true
    })
  })
}