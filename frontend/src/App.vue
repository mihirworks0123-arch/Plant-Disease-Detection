<template>
  <div class="app">
    <!-- <Navbar/> -->
    <router-view/>
  </div>
  
</template>

<script>
import Navbar from "../src/components/Navbar.vue"
export default {
  name: "App",
  components: {
    Navbar,
  }

}
</script>

<style>
@import "../src/assets/css/app.css"

</style>