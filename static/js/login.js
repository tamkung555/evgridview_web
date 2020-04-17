function login() {

    if (document.getElementById("username").value == '' && document.getElementById("password").value) {
          alert("Please enter username or password!!!")
        } else {
          login_data = JSON.stringify({
            username: document.getElementById("username").value,
            password: document.getElementById("password").value
          })
          var spinner = $('#loader');
          spinner.show();      
          console.log(login_data)
          console.log("POST Login method by jQuery")
          jQuery.ajax({
              url: "https://cors-anywhere.herokuapp.com/https://msr-api.herokuapp.com/api/login",
              type: "POST",
              headers: {
                "Content-Type": "application/x-www-form-urlencoded",
                "Access-Control-Allow-Origin": "https://cors-anywhere.herokuapp.com/https://msr-api.herokuapp.com/api/login",
                "Access-Control-Allow-Methods": "POST",
                "Access-Control-Allow-Headers": "Content-Type, Authorization",  
              },
              contentType: "application/x-www-form-urlencoded",
              data: {
                "username": document.getElementById("username").value.toString(),
                "password": document.getElementById("password").value.toString()
            },
          })
            .done(function(data, textStatus, jqXHR) {
              console.log("HTTP Request Succeeded: " + jqXHR.status);
              console.log(data);
              if (jqXHR.status == 200) {
                spinner.hide();
                console.log("Login successful.");
                // storeToken(data);
                // localStorage.setItem("token_local", data['token']);
                window.location.replace("./views/home.html");
              }
            })
            .fail(function(jqXHR, textStatus, errorThrown) {
              console.log("HTTP Request Failed");
              alert("Usernamr or Password is wrong. Please try again!!!")
            })
            .always(function() {
            });
          }
    }
  
    function storeToken(data) {
      document.cookie = encodeURIComponent('token') + '=' + encodeURIComponent(data['data']['token']) + ';';
      // document.write(document.cookie);
      // alert( document.cookie )
      window.location.replace("./views/home.html");
  
    }