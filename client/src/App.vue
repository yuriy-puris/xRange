<template>
  <v-app>
      <Header />
      <v-container>
        <Search />
      </v-container>
      <Footer />
  </v-app>
</template>

<script>
import Header from '@/components/Shared/Header'
import Footer from '@/components/Shared/Footer'
import Search from '@/components/Shared/Search'

export default {
  name: 'App',
  components: {
    Header,
    Footer,
    Search
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
