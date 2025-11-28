<template>
    <div class="dashboard">
      
      <section class="one">
        <Navbar />
        <div class="content">
          <div data-aos="fade-right" data-aos-duration="1000" data-aos-delay="0" data-aos-offset="1"><small>Try out</small></div>
          <div data-aos="fade-left" data-aos-duration="1000" data-aos-delay="250" data-aos-offset="1"><h1>Our Yolov8</h1></div>
          <div data-aos="fade-right" data-aos-duration="1000" data-aos-delay="500" data-aos-offset="1"><h1>Models</h1></div>
          <div data-aos="fade-right" data-aos-duration="1000" data-aos-delay="750" data-aos-offset="10">Please click on the crop which you need to detect</div>
        </div>
      </section>
      <div>
        <!-- <h2>Dashboard</h2> -->
        <!-- <div class="content mt-5">Please click on the crop which you need detection with. And then upload your image on the next page</div> -->
        <div class="container mt-5">
          <div class="row">
            <div v-for="(crop, index) in crops" :key="index" class="col-sm-4" data-aos="fade-left" data-aos-duration="1000" data-aos-delay="500">
              <router-link :to="{ name: 'Crop', params: { crop_name: crop.name } }">
                  <div class="crop-box" @mouseover="showCropName(index)" @mouseout="hideCropName(index)">
                    <img :src="crop.image" alt="Crop Image" class="img-fluid">
                    <div class="crop-info">
                      <h5 v-show="hoveredCropIndex === index">{{ crop.name }}</h5>
                    </div>
                  </div>
              </router-link>
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div>
</template>

<script>
import Navbar from "../components/Navbar.vue"
import Footer from "../components/Footer.vue"
export default {
  name: "Dashboard",
  components: {
    Navbar,
    Footer
  },
  data() {
    return {
    crops: [
      { name: "Bhindi", image: require("@/assets/crops/bhindi.jpg") },
      { name: "Gourd", image: require("@/assets/crops/gourd.jpg") },
      { name: "General", image: require("@/assets/crops/general.jpg") },
      { name: "EggPlant", image: require("@/assets/crops/eggplant.jpg") },
      { name: "Potato", image: require("@/assets/crops/potato.jpg") },
      { name: "Corn", image: require("@/assets/crops/corn.jpg") },
      // Add more crops as needed
    ],
    hoveredCropIndex: null,
    };
  },
  methods: {
    showCropName(index) {
      this.hoveredCropIndex = index;
    },
    hideCropName() {
      this.hoveredCropIndex = null;
    },
  }
}
</script>

<style scoped>

.content {
  /* color: #fbfcfd;  #404464 #FF8D5C */
  color: #fbfcfd;
  position: absolute;
  top: 50%;
  left: 8%;
  transform: translateY(-50%);
  font-size: 20px;
}

h1 {
  font-size: 80px;
  line-height: 70px;
  margin: 10px 0 30px;
}

.crop-box {
  position: relative;
  overflow: hidden;
  margin-bottom: 20px;
}

.crop-box img {
  transition: transform 0.3s ease;
  max-width: 100%;
  max-height: 100%;
}

.crop-info {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.crop-info h5 {
  margin: 0;
}

.crop-box:hover img {
  transform: scale(1.1);
}

.crop-box:hover .crop-info {
  opacity: 1;
}

img {
  height: 200px;
  width: 450px;
}

body {
  background-color: #d8f3dc;  /* Light green background */
  color: #2a9d8f;            /* Dark green text color */
  
}

.one {
  background-image: url('../assets/background/plant11.jpg');
  width: 100%;
  height: 100vh;
  z-index: 0;
  background-size: cover;
  background-position: center;
  position: relative; 
  overflow: hidden; 
  color: white;
}


</style>