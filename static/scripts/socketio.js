  document.addEventListener('DOMContentLoaded', () => {
  	
    // Connecting to websocket
    var socket = io();



    // Setting default room
  	let room = "GlobalChat";
  	joinRoom("GlobalChat");

  	// Displaying Messages
    socket.on('message', data => {

        // Display current message
        if (data.msg) {
        	const p = document.createElement('p');
            const span_username = document.createElement('span');
            const span_timestamp = document.createElement('span');
            const br = document.createElement('br')

            // Message from current user
            if (data.username == username) {
                p.setAttribute("class", "my-msg");

                // Username
                span_username.setAttribute("class", "my-username");
            	span_username.innerHTML = data.username;
        		
                // Timestamp
                span_timestamp.setAttribute("class", "timestamp");
                span_timestamp.innerHTML = data.time_stamp;

                // Showing message
        		p.innerHTML += span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML 
        		+ span_timestamp.outerHTML;

        		document.querySelector('#display-message-section').append(p);
            }
            // Display other users' messages
            else if (typeof data.username !== 'undefined') {
                p.setAttribute("class", "others-msg");

                // Username
                span_username.setAttribute("class", "other-username");
                span_username.innerText = data.username;

                // Timestamp
                span_timestamp.setAttribute("class", "timestamp");
                span_timestamp.innerText = data.time_stamp;

                // HTML to append
                p.innerHTML += span_username.outerHTML + br.outerHTML + data.msg + br.outerHTML + span_timestamp.outerHTML;

                //Append
                document.querySelector('#display-message-section').append(p);
            }

            // System message display
            else {
            	printSysMsg(data.msg);
            }
        }
        scrollDownChatWindow();

    });

    // Used with emit from app.py
    // socket.on('some-event', data => {
    // 	console.log(data);
    // });

    // Sending Messages
    document.querySelector('#send_message').onclick = () => {
    	socket.send({'msg': document.querySelector('#user_message').value, 'username': username, 'room': room})

    	// Clearing Message Type Box
    	document.querySelector('#user_message').value = '';
    }

    // Selecting Rooms
    document.querySelectorAll('.room-selection').forEach(p => {
    	p.onclick = () => {
    		let newRoom = p.innerHTML;

    		// Checking if user is already in a room
    		if (newRoom == room) {
    			msg = `Already present in room ${room}.`
    			printSysMsg(msg);
    		}
    		else {
    			leaveRoom(room);
    			joinRoom(newRoom);
    			room = newRoom;
    		}
    	}
    });

    // Logout from chat
    document.querySelector("#logout-btn").onclick = () => {
        leaveRoom(room);
    };

    // Logout from chat
    document.querySelector("#home-btn").onclick = () => {
        leaveRoom(room);
    };

    // Leave Room Function
    function leaveRoom(room) {
    	socket.emit('leave', {'username': username, 'room': room});
        
        document.querySelectorAll('.room-selection').forEach(p => {
            p.style.color = "black";
        });
    }

    // Join Room Function
    function joinRoom(room) {
    	socket.emit('join', {'username': username, 'room': room});

        // Highlight selected room
        document.querySelector('#' + CSS.escape(room)).style.color = "#ffc107";
        document.querySelector('#' + CSS.escape(room)).style.backgroundColor = "white";

    	// Clearing Message Box
    	document.querySelector('#display-message-section').innerHTML = ''

    	// Autofocusing on TextBox
    	document.querySelector('#user_message').focus();
    }

    // Scroll chat window down
    function scrollDownChatWindow() {
        const chatWindow = document.querySelector("#display-message-section");
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    // Printing System Messages
    function printSysMsg(msg) {
    	const p = document.createElement('p');
        p.setAttribute("class", "system-msg");
        p.innerHTML = msg;
        document.querySelector('#display-message-section').append(p);
        scrollDownChatWindow()

        // Autofocus on text box
        document.querySelector("#user_message").focus();
    }
 });
