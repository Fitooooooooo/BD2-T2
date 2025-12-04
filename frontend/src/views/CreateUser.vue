<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-title class="text-h5">Crear Nuevo Usuario</v-card-title>
          <v-card-text>
            <v-form @submit.prevent="submitForm">
              <v-text-field
                v-model="username"
                label="Nombre de Usuario"
                required
                :rules="[v => !!v || 'El nombre de usuario es requerido']"
              ></v-text-field>
              <v-text-field
                v-model="fullname"
                label="Nombre Completo"
                required
                :rules="[v => !!v || 'El nombre completo es requerido']"
              ></v-text-field>
              <v-text-field
                v-model="password"
                label="Contraseña"
                type="password"
                required
                :rules="[v => !!v || 'La contraseña es requerida']"
              ></v-text-field>
              <v-btn type="submit" color="primary" class="mt-4" :loading="loading">Crear Usuario</v-btn>
            </v-form>
            <v-alert v-if="error" type="error" class="mt-4" closable>{{ error }}</v-alert>
            <v-alert v-if="success" type="success" class="mt-4" closable>{{ success }}</v-alert>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { createUser } from '@/api'
import type { User } from '@/interfaces'

const router = useRouter()

const username = ref('')
const fullname = ref('')
const password = ref('')
const error = ref<string | null>(null)
const success = ref<string | null>(null)
const loading = ref(false)

async function submitForm() {
  error.value = null
  success.value = null
  loading.value = true
  try {
    const newUser: Omit<User, 'id'> & { password: string } = {
      username: username.value,
      fullname: fullname.value,
      password: password.value,
    }
    await createUser(newUser)
    success.value = 'Usuario creado exitosamente. Redireccionando...'
    setTimeout(() => router.push({ name: 'home' }), 2000)
  } catch (err: any) {
    console.error('Error al crear el usuario:', err)
    error.value = err.message || 'Error al crear el usuario. Inténtalo de nuevo.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
</style>
