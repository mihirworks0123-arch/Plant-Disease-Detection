<template>
  <div class="about">
    <Navbar />

    <!-- First Section -->
    <section class="section bg-light d-flex" id="device">
      <div class="container">
        <div class="row align-items-center mt-5 offset-sm-2">
          <div class="col-sm-6 d-flex flex-column justify-content-center align-items-center" data-aos="fade-up-right" data-aos-duration="2000" data-aos-offset="100">
            <h1 style="color: rgba(123, 123, 123, 0.7); font-size: 40px; line-height: 40px;">Mihir Mengde</h1>
            <p class="text-muted my-4">
              As a passionate student and Coding Connoisseur in Machine Learning and AI, I excel in Python and dabble in various programming languages. My skills foster learning through real-life examples, active listening, contemporary insights, creative thinking, synthesis, and multimedia research.
            </p>
          </div>

          <div class="col-sm-6 d-flex flex-column justify-content-center align-items-center" data-aos="fade-up-left" data-aos-duration="2000" data-aos-offset="100">
            <img class="img-fluid rounded" src="../assets/photos/mihir.jpeg" alt="" width="150" height="150" />
          </div>
        </div>
        <!-- end row -->
      </div>
      <!-- end container -->
    </section>

    <!-- Second Section -->
    <section class="section bg-light justify-content-center align-items-center" id="device">
      <div class="container">
        <div class="row align-items-center mt-2 offset-sm-2">
          <div class="col-sm-6 d-flex flex-column justify-content-center align-items-center" data-aos="fade-up-right" data-aos-duration="2000" data-aos-offset="100">
            <h1 style="color: rgba(123, 123, 123, 0.7); font-size: 40px; line-height: 40px;">Rishabh Jain</h1>
            <p class="text-muted my-4">
              Master Data Maestro excelling in Data Science, navigating networks, and operating systems. Elevates leadership and teamwork through seamless communication and expert insights. Proficient in literature review, cross-referencing, and self-management. Adept at synthesizing information for enhanced decision-making.
            </p>
          </div>

          <div class="col-sm-6 d-flex flex-column justify-content-center align-items-center" data-aos="fade-up-left" data-aos-duration="2000">
            <img class="img-fluid rounded" src="../assets/photos/rishabh.jpeg" alt="" width="150" height="150" />
          </div>
        </div>
        <!-- end row -->
      </div>
      <!-- end container -->
    </section>

    <!-- Third Section -->
    <section class="section bg-light justify-content-center align-items-center" id="device">
      <div class="container">
        <div class="row align-items-center mt-2 offset-sm-2">
          <div class="col-sm-6 d-flex flex-column justify-content-center align-items-center" data-aos="fade-up-right" data-aos-duration="2000" data-aos-offset="100">
            <h1 style="color: rgba(123, 123, 123, 0.7); font-size: 40px; line-height: 40px;">Vaibhav Hawaldar</h1>
            <p class="text-muted my-4">
              Python-proficient Data Science Dynamo adept in Data Analysis and Machine Learning. Eager to bolster team dynamics with a commitment to diverse perspectives, clear communication, efficient information management, and adept knowledge synthesis. Ready to contribute expertise for a collaborative and high-impact environment.
            </p>
          </div>

          <div class="col-sm-6 d-flex flex-column justify-content-center align-items-center" data-aos="fade-up-left" data-aos-duration="2000" data-aos-offset="100">
            <img class="img-fluid rounded" src="../assets/photos/vaibhav.png" alt="" width="150" height="150" />
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
  name: "AboutUs",
  components: {
    Navbar,
    Footer
  },
}
</script>

<style scoped>
h2 {
  text-align: center;
  /* color:#d8f3dc; */
}

img{
  border-radius: 50%;
  height: 200px;
  width: 200px;
}
.info-container {
  display: flex;
  align-items: center;
}
.info {
  padding: 10px;
  border: 1px solid #ccc;
}

body {
  background-color: #d8f3dc;  /* Light green background */
  color: #2a9d8f;            /* Dark green text color */
}

</style>