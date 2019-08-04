<template>
    <v-form v-model="valid">
        <v-container grid-list-xl>
            <v-layout wrap>
                <v-flex>
                    <v-text-field
                        v-model="searchProduct"
                        label="Search product ...">
                        
                    </v-text-field>
                </v-flex>
            </v-layout>
        </v-container>
    </v-form>
</template>

<script>
export default {
    name: 'Search',
    data() {
        return {
            searchProduct: ''
        }
    }
}
</script>

<style lang="sass">
    
</style>