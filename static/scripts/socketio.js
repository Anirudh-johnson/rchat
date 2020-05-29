document.addEventListener('DOMContentLoaded', () =>{
  var socket =io('http://' + document.domain + ':' + location.port);

  let room = "lounge";
  joinRoom(room);
    // Display incoming messages
    socket.on('message', data =>{
    const p = document.createElement('p');
    const span_username = document.createElement('span');
    const span_timestamp = document.createElement('span');
    const br = document.createElement('br');

    if (data.username) {span_username.innerHTML = data.username;
    span_timestamp.innerHTML = data.time_stamp;
    p.innerHTML = span_username.outerHTML + br.outerHTML + data.msg +br.outerHTML + span_timestamp.outerHTML;

    document.querySelector('#display-message-section').append(p);
  } else {
    printSysMsg(data.msg)
  }


  });

  // Send messages
  document.querySelector('#send_message').onclick = () => {
    socket.send({'msg': document.querySelector('#user_message').value,'username':username, 'room': room});

    document.querySelector('#user_message').value = '';


  }


  // Joining and leaving Rooms
  document.querySelectorAll('.Select-rooms').forEach( p => {
    p.onclick = () => {
      let newRoom = p.innerHTML;
      if (newRoom == room) {
        msg = `You are already in ${room} room.`;
        printSysMsg(msg);
      } else {
        leaveRoom(room);
        joinRoom(newRoom);
        room = newRoom;
      }
    }
  });
  // Leave Room
  function leaveRoom(room) {
    socket.emit('leave', {'username' : username, 'room' : room});
  }
  function joinRoom(room) {
    socket.emit('join', {'username' : username, 'room' : room});
    // Clear message area
    document.querySelector('#display-message-section').innerHTML = '';
    // Autofocus on input area 
    document.querySelector('#user_message').focus();
  }
  //Print system messages
  function printSysMsg(msg) {
    const p = document.createElement('p');
    p.innerHTML = msg;
    document.querySelector('#display-message-section').append(p);
  }
})
