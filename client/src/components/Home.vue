<template>
  <h2>{{ msg }}</h2>
</template>
<script>
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
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
      count = 6;
    } else {
      count = params.get('len');
    }
    this.getMessage(count);
  },
};
</script>
