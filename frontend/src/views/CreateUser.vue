<script setup lang="ts">
import UserForm from '@/components/UserForm.vue'
import type { User } from '@/interfaces'
import { useRouter } from 'vue-router'
import { createUser } from '@/api'

const router = useRouter()

async function handleSaveUser(userData: User) {
  try {
    await createUser(userData)
    router.push({ name: 'home' })
  } catch (error) {
    console.error('Error al crear el usuario:', error)
  }
}
</script>

<template>
  <UserForm @save-user="handleSaveUser" />
</template>