<template>
    <div class="container mx-auto">
      <div class="row g-4">
        <div class="col main-left">
          <div class="p-4 bg-white border border-1 border-secondary rounded">
            <h1 class="mb-4 fs-3">Register to become a member!</h1>
  
            <p class="mb-4 text-muted">
              Welcome to <strong>Vocabularious</strong>! 
            </p>

            <p class="mb-4 text-muted">
            Please fill in the form provided to register as a member.
              By signing up, you will have full access to our site and be able to contribute to numerous surveys.
            </p>
  
            <p class="mb-4 text-muted">
              Regardless of whether you are a seasoned researcher or a curious individual interested in exploring the field of lexical variation,
               we welcome you to take interest and join us!
            </p>

            <p class="fw-bold">
              Already have an account? Click here to log in!
            </p>
          </div>
        </div>
  
        <div class="col main-right">
          <div class="p-4 bg-white border border-1 border-secondary rounded">
            <form>
              <div class="mb-4">
                <label>Name</label><br>
                <input type="text" placeholder="Enter your name..." class="form-control mt-2">
              </div>

              <div class="mb-4">
                <label>City</label><br>
                <input type="text" placeholder="Your location..." class="form-control mt-2">
              </div>
  
              <div class="mb-4">
                <label>Username</label><br>
                <input type="text" placeholder="Create a username..." class="form-control mt-2">
              </div>
  
              <div class="mb-4">
                <label>Password</label><br>
                <input type="password" placeholder="Create a password..." class="form-control mt-2">
              </div>
  
              <div class="mb-4">
                <label>Repeat password</label><br>
                <input type="password" placeholder="Confirm password..." class="form-control mt-2">
              </div>
  
              <div>
                <button class="btn btn-primary">Sign up</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  