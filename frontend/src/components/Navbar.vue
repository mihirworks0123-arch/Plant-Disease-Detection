<template>
  <div class="nav">
    <nav class="navbar navbar-expand-sm navbar-light" style="background-color: rgba(144, 238, 144, 0.7);">
      <div class="container">
        <router-link class="navbar-brand" style="color: white;" :to="{name: 'Dashboard'}">SOULLEAF</router-link>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <router-link class="btn button" :to="{name: 'Home'}">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link class="btn button" :to="{name: 'Dashboard'}">Dashboard</router-link>
            </li>
            <li class="nav-item">
              <router-link class="btn button" :to="{name: 'AboutUs'}">About Us</router-link>
            </li>
            <li class="nav-item">
              <router-link class="btn button" :to="{name: 'ProjectDetails'}">Project Details</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </div>
</template>

<style>
.nav {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.navbar {
  width: 85%;
}

.nav .button {
  color: #fbfcfd;
  padding: 10px 25px;
  background: transparent;
  border: 1px solid #fff;
  border-radius: 20px;
  outline: none;
  margin-right: 10px;
}

.white-text {
  color: white;
}
</style>
