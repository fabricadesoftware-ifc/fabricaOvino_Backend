<template>
  <div>
    <Header />
    <div class="tile is-ancestor">
      <div class="tile is-parent is-2">
        <Menu />
      </div>
      <div class="tile is-parent">
        <div class="tile is-child is-11">
          <nuxt />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "./Header";
import Menu from "./Menu";
export default {
  components: { Header, Menu },
};
</script>

<style>
* {
  font-family: "Lato", sans-serif;
}
body {
  margin: 0;
}

#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  height: 100vh;
  /* display: grid;
  grid-template-rows: 60px 1fr 40px;
  grid-template-columns: 300px 1fr;
  grid-template-areas:
    "header header"
    "menu content"
    "menu footer"; */
}
</style>
