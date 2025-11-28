<template>
  <div class="details">
    <Navbar />
    <section class="section bg-light d-flex" id="device">
      <div class="container">
        <div class="row align-items-center mt-5">
          <div class="col-sm-6 d-flex flex-column justify-content-center align-items-center" data-aos="fade-up-left" data-aos-duration="2000" data-aos-offset="100">
            <h1>Research Paper</h1>
          </div>
          <div class="col-sm-6 d-flex flex-column justify-content-center align-items-center" data-aos="fade-up-right" data-aos-duration="2000" data-aos-offset="100">
            <h1 style="color: rgba(123, 123, 123, 0.7); font-size: 20px; line-height: 20px;">Paper</h1>
            <p class="text-muted my-4">
              This research project focuses on the comparative analysis between two advanced deep learning models, You Only Look Once Version 8 (YOLOv8) andcd  YOLOv5 model, in the context of plant leaf disease detection within the agricultural sector. The study highlights the significance of early disease detection for maximizing agricultural outcomes and addresses the limitations of traditional scouting methods. Leveraging deep learning, particularly the undisclosed model, the research introduces a custom-annotated dataset to assess the models' performance comprehensively.
            </p>
          </div>
        </div>
        <!-- end row -->
      </div>
      <!-- end container -->
    </section>


    <section class="section bg-light d-flex" id="device">
      <div class="container">
        <div class="row align-items-center mt-5">
          <div class="col-sm-6 d-flex flex-column justify-content-center align-items-center" data-aos="fade-up-left" data-aos-duration="2000" data-aos-offset="100">
            <h1>Application</h1>
          </div>
          <div class="col-sm-6 d-flex flex-column justify-content-center align-items-center" data-aos="fade-up-right" data-aos-duration="2000" data-aos-offset="100">
            <h1 style="color: rgba(123, 123, 123, 0.7); font-size: 20px; line-height: 20px;">Backend</h1>
            <p class="text-muted my-4">
              The website's backend is powered by Flask, a Python web framework renowned for its simplicity and flexibility. Flask allows for the seamless integration of our YOLOv8 model and facilitates the handling of user requests and image processing. Through Flask, we have created a robust and reliable backend infrastructure to support the core functionality of our platform.

            </p>

            <h1 style="color: rgba(123, 123, 123, 0.7); font-size: 20px; line-height: 20px;">Frontend</h1>
            <p class="text-muted my-4">
              The frontend of our website is designed using Vue.js, a progressive JavaScript framework. Vue.js excels in creating dynamic and interactive user interfaces. It provides a smooth and responsive user experience, enabling users to interact with our platform intuitively. The use of Vue.js ensures that our website is not only functional but also visually appealing and user-friendly.

            </p>
          </div>
        </div>
        <!-- end row -->
      </div>
      <!-- end container -->
    </section>
    <Footer />  
  </div>
</template>

<script>
import Navbar from "../components/Navbar.vue"
import Footer from "../components/Footer.vue"
export default {
  name: "ProjectDetails",
  components: {
    Navbar,
    Footer
  },
}
</script>

<style scoped>

body{
  margin: 0;
  padding: 0;
  
}


</style>