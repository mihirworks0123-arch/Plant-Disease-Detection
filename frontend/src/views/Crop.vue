<template>
    <div class="container text-center">
      <Navbar />
      <div class="whole mx-auto d-flex align-items-center flex-column">
          <p>Upload {{ crop_name }} image to check if it is diseased or not</p>
          
          <div class="img_svg mt-4">
              <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="currentColor" class="bi bi-images" viewBox="0 0 16 16">
                  <path d="M4.502 9a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3z"/>
                  <path d="M14.002 13a2 2 0 0 1-2 2h-10a2 2 0 0 1-2-2V5A2 2 0 0 1 2 3a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v8a2 2 0 0 1-1.998 2zM14 2H4a1 1 0 0 0-1 1h9.002a2 2 0 0 1 2 2v7A1 1 0 0 0 15 11V3a1 1 0 0 0-1-1zM2.002 4a1 1 0 0 0-1 1v8l2.646-2.354a.5.5 0 0 1 .63-.062l2.66 1.773 3.71-3.71a.5.5 0 0 1 .577-.094l1.777 1.947V5a1 1 0 0 0-1-1h-10z"/>
              </svg>
          </div><br>
  
          <form enctype="multipart/form-data" class="d-flex flex-column align-items-center">
              <input type="file" class="form-control" name="file" ref="inputFile" size="4"/><br>
              <button type="submit" class="form-control btn btn-info" @click.prevent="Uploadfile">Upload</button>
          </form>
      </div>
  
    </div>
  </template>

<script>
import router from '../router/index'
import Navbar from "../components/Navbar.vue"
// import Footer from "../components/Footer.vue"
export default {
    name: "Crop",
    components: {
        Navbar,
        // Footer
    },
    data() {
        return {
            crop_name: "",
        }
    },
    mounted() {
        this.crop_name = this.$route.params.crop_name;
        // console.log(this.crop_name);
    },
    methods: {
        async Uploadfile(event) {
            event.preventDefault()
            let formData = new FormData();
            // console.log(this.$refs.inputFile);
            formData.append('file', this.$refs.inputFile.files[0]);
            // axios.post('/upload/' + this.crop_name, formData)
            // let response = fetch(`http://127.0.0.1:5000/upload/${this.crop_name}`, {
            //     method: 'POST',
            //     body: formData
            // })
            // /upload/new_model/<crop_name>
            if (this.crop_name == "EggPlant" || this.crop_name == "Potato" || this.crop_name == "Corn") {
                const response = await fetch(`http://127.0.0.1:5000/upload/new_model/${this.crop_name}`, {
                    method: 'POST',
                    body: formData
                })
                if (response.ok) {
                    const data = await response.json();
                    console.log('File uploaded successfully');
                    alert("File uploaded successfully")
                    router.push({ 
                        name: 'Result',
                        query: { 
                            class_label: data.class_label,
                            confidence: data.confidence,
                            total_spots: data.total_spots
                        }
                    });
                } else {
                    console.error('Error uploading file')
                }
            }
            else{
                const response = await fetch(`http://127.0.0.1:5000/upload/${this.crop_name}`, {
                    method: 'POST',
                    body: formData
                })
                if (response.ok) {
                    const data = await response.json();
                    console.log('File uploaded successfully');
                    alert("File uploaded successfully")
                    router.push({ 
                        name: 'Result',
                        query: { 
                            class_label: data.class_label,
                            confidence: data.confidence,
                            total_spots: data.total_spots
                        }
                    });
                } else {
                    console.error('Error uploading file')
                }
            }
            
        }
    },

}
</script>

<style scoped>
form {
    display: flex;
    align-content: center;
    align-items: center;
}

.whole {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    height: 90vh; /* Optional: Set height to fill the viewport */
  }
</style>