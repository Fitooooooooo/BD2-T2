<script setup lang="ts">
import UserList from '@/components/UserList.vue'
</script>

<template>
    <v-container>
        <div class="d-flex justify-end mb-4">
            <v-btn color="primary" prepend-icon="mdi-plus" :to="{ name: 'userCreate' }">Crear Usuario</v-btn>
        </div>
        <UserList />
    </v-container>
</template>
