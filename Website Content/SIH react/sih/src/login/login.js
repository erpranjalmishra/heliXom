document.addEventListener('DOMContentLoaded', function () {
    // Select the login button
    const loginButton = document.querySelector('.login-btn');
    
    // Select the input fields for username and password
    const usernameInput = document.querySelector('input[type="text"]');
    const passwordInput = document.querySelector('input[type="password"]');

    loginButton.addEventListener('click', function (event) {
        
        event.preventDefault();

      
        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();

     
        if (username === '' || password === '') {
        
            alert('Please enter both username and password.');
        } else {
           
            alert(`Welcome, ${username}!`);
            
        }
    });

    // Event listeners to clear and restore placeholder text for username input
    usernameInput.addEventListener('focus', function () {
        this.placeholder = '';
    });
    usernameInput.addEventListener('blur', function () {
        this.placeholder = 'Username';
    });

    // Event listeners to clear and restore placeholder text for password input
    passwordInput.addEventListener('focus', function () {
        this.placeholder = '';
    });
    passwordInput.addEventListener('blur', function () {
        this.placeholder = 'Password';
    });
});