<script>

</script>

<template>
    <div class="container">
      <div class="row g-5">
        <div class="col-lg-6 main-left">
          <div class="p-4 bg-light border border-1 border-secondary rounded">
            <h1 class="mb-4 display-4">Login to your account!</h1>
  
            <p class="mb-4 fst-italic text-muted">
              Welcome to <strong>Vocabularious</strong>!
            </p>
  
            <p class="mb-4 text-muted">
              Please enter your login credentials to access your account.
            </p>
  
            <p class="fw-bold"><small>
              Don't have an account yet? Click <RouterLink to="/register" class="text-primary"><mark>here</mark></RouterLink> to register!
            </small>
            </p>
          </div>
        </div>
  
        <div class="col-lg-6 main-right">
          <div class="p-4 bg-white border border-1 border-secondary rounded">
            <form>
              <div class="mb-3">
                <label class="form-label">Username</label>
                <input type="text" placeholder="Enter your username..." class="form-control">
              </div>
  
              <div class="mb-3">
                <label class="form-label">Password</label>
                <input type="password" placeholder="Enter your password..." class="form-control">
              </div>

              <div>
                <button class="btn btn-primary">Log in</button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </template>
  