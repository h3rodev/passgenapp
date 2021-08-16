<template>
<main>
  <header>  
    <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
      <a class="navbar-brand" href="#">SPG App</a>
    </nav>
  </header>

  <router-view/>

  <footer class="footer">
    <div class="container text-center">
      <span class="text-muted ">App by <a href="https://github.com/h3rodev">h3rodev</a></span>
    </div>
  </footer>

</main>
</template>
<style>

html {
  position: relative;
  min-height: 100%;
}
body {

  margin-bottom: 60px;
}
.footer {
  position: absolute;
  bottom: 0;
  width: 100%;

  height: 60px;
  line-height: 60px; 
  background-color: #f5f5f5;
}

body > .container,
body > main  {
  padding: 60px 15px 0;
}

.footer > .container {
  padding-right: 15px;
  padding-left: 15px;
}

.navbar {
  padding: 1.75rem !important;
}
.navbar-brand {
    position: absolute;
    left: 50%;
    margin-left: -50px !important;  /* 50% of your logo width */
    display: block;
}
.custom-slider {
    align-self: center;
    display: flex;
    flex-flow: column;
    align-items: center;
}

</style>

