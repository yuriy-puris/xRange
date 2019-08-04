<template>
    <v-app-bar app>
        <v-toolbar-title>
            xRates
        </v-toolbar-title>
        <v-spacer></v-spacer>
        <v-toolbar-items>
            <v-btn text>Link 1</v-btn>
            <v-btn text>Link 2</v-btn>
            <v-btn text>Link 3</v-btn> 
        </v-toolbar-items>
    </v-app-bar>
</template>

<script>
export default {
    name: 'Header',
    data() {
        return {
            header: 'header test 2'
        }
    }
}
</script>

<style lang="sass">
    
</style>