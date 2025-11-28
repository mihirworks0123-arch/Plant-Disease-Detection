<template>
  <div class="result">
    <Navbar />
    <h1 class="mt-5">This is result</h1>
    <div class="image-container">
      <img :src="imgSrc" alt="Annotated Image" class="centered-image"/>
    </div>
    <h4>Result details are:</h4>
    <p>
      <strong>Label: {{ class_label }} <br> Spots: {{ total_spots }} <br> Confidence: {{ confidence }} </strong>
    </p>
    
  </div>
</template>

<script>
import router from '../router/index'  
import Navbar from "../components/Navbar.vue"
export default {
  name: "Result",
  components: {
    Navbar,
    // Footer
  },
  data() {
    return {
      imgSrc: "",
      class_label: "",
      confidence: "",
      total_spots: "",
    }
  },
  mounted() {
    this.fetchImage();

    this.class_label = this.$route.query.class_label;
    this.confidence  = this.$route.query.confidence ;
    this.total_spots = this.$route.query.total_spots;
  },
  methods: {
    async fetchImage() {
      var path = "http://127.0.0.1:5000/result"
      try {
        const response = await fetch(path, {
          method: "GET",
        });

        if (response.ok) {
          // Assume the response contains the image URL
          // this.imageSrc = response.url;
          const blob = await response.blob();
          const dataUrl = URL.createObjectURL(blob);

          // Set the data URL as the image source
          this.imgSrc = dataUrl;
        } else {
          console.error("Failed to fetch image");
        }
      } catch (error) {
        console.error("Error fetching image:", error);
      }
    },
  }
}
</script>

<style scoped>
.result {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.image-container {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 20px; /* Adjust margin as needed */
}

.centered-image {
  max-width: 100%; /* Ensure the image doesn't exceed its container's width */
  max-height: 100%; /* Ensure the image doesn't exceed its container's height */
}
</style>