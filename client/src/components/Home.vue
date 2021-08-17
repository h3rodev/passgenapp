<template>
  <div class="container text-center">
    <h1 class="mt-5 mb-5">Secure Password Generator</h1>
    <div class="card">
      <div class="card-body">
        <h4>{{ msg }}</h4>
      </div>
    </div>
    <div class="custom-slider mt-5">
      <RoundSlider 
        v-model="sliderValue"
        start-angle="315"
        end-angle="+270"
        line-cap="round"
        step="2"
        min="6"
        max=128
        radius="120"
      />
      <span>Password Length</span>
      <a class="btn btn-primary mt-3" href="#" role="button" @click="genpassword">Generate Password</a>
    </div>
  </div>
</template>
<script>
import axios from 'axios';
import RoundSlider from 'vue-round-slider';

export default {
  name: 'Home',
  data() {
    return {
      msg: '',
      sliderValue: 6
    };
  },
  components: {RoundSlider},
  methods: {
    genpassword: function(e){
      e.preventDefault();

      const uri = window.location.search.substring(1);
      const params = new URLSearchParams(uri);

      let count = 0;
      if (!params.get('len')) {
        count = this.sliderValue;
      } else {
        count = params.get('len');
      }
      this.getMessage(count);
    },
    getMessage(l) {
      const path = `http://localhost:5000/api/gen/${String(l)}`;
      axios.get(path)
        .then((res) => {
          this.msg = res.data.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    const uri = window.location.search.substring(1);
    const params = new URLSearchParams(uri);

    let count = 0;
      if (!params.get('len')) {
        count = this.sliderValue;
      } else {
        count = params.get('len');
      }
    this.getMessage(count);
  },
};
</script>
