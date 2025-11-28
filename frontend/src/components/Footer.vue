<template>
    <div class="foot">
      <footer class="text-center text-lg-start text-white" style="background-color: rgb(81, 221, 132); padding: 10px; margin-top: 10px; font-size: 14px;">
        <!-- Right -->
  
        <!-- Section: Links  -->
        <section class="container-fluid">
          <div class="container text-center text-md-start mt-3">
            <!-- Grid row -->
            <div class="row mt-2">
              <!-- Grid column -->
              <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-2">
                <!-- Content -->
                <h6 class="fw-bold">SOULLEAF</h6>
                <hr class="mb-1 mt-0 d-inline-block mx-auto" style="width: 40px; background-color: #7c4dff; height: 1px;">
                <p>Empowering Nature's Guardians: Protecting Plants with the best Organic way possible</p>
              </div>
              <!-- Grid column -->
  
              <!-- Grid column -->
              <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-2">
                <!-- Links -->
                <h6 class="text-uppercase fw-bold">Contact</h6>
                <hr class="mb-1 mt-0 d-inline-block mx-auto" style="width: 40px; background-color: #7c4dff; height: 1px;">
                <p><i class="bi bi-house"></i> Mumbai-401107, IND</p>
                <p><i class="bi bi-envelope"></i> info@SOULLEAF.com</p>
                <p><i class="bi bi-telephone"></i> 1800 100 100</p>
              </div>
              <!-- Grid column -->
            </div>
            <!-- Grid row -->
          </div>
        </section>
        <!-- Section: Links  -->
  
        <!-- Copyright -->
        <div class="text-center p-2" style="background-color: rgba(0, 0, 0, 0.2); font-size: 12px;">
          ©️ 2023 Copyright:
          <router-link :to="{name: 'Home'}">Home</router-link>
        </div>
        <!-- Copyright -->
      </footer>
  
      <div id="content" class="site-content center-relative"> </div>
    </div>
  </template>
  

<script>
export default {
    name: "Footer"

}
</script>

<style>

</style>