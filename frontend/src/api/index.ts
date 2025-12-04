import type { LoginResponse, User } from '@/interfaces'
import { useAuthStore } from '@/stores/auth'

const API_BASE_URL = "http://localhost:8000"

export async function apiFetch(path: string, config: Record<string, any>) {
    const auth = useAuthStore()
    const defaultHeaders: Record<string, string> = {}

    if (auth.token) {
        defaultHeaders['Authorization'] = `Bearer ${auth.token}`
    }

    config.headers = { ...defaultHeaders, ...config.headers }
    return await fetch(`${API_BASE_URL}${path}`, config)
} 

export async function login(
    username: string,
    password: string,
): Promise<LoginResponse | undefined> {
    const body = new URLSearchParams({
        username: username,
        password: password,
    })
    const response = await fetch('http://localhost:8000/auth/login', {
        method: 'POST',
        body: body,
    })
    if (response.ok) {
        return await response.json()
    }
}

export async function fetchUsers(): Promise<User[]> {
    const response = await apiFetch('/users', {
        cache: 'no-cache',
    })
    return await response.json()
}

export async function fetchUser(
    id: number,
): Promise<User | null> {
    const response = await apiFetch(`/users/${id}`, {})
    return await response.json()
}

export async function patchUser(
    id: number,
    userData: User,
) {
    const response = await apiFetch(`/users/${id}`, {
        method: 'PATCH',
        body: JSON.stringify(userData),
    })
    return await response.json()
}

export async function createUser(
    userData: Omit<User, 'id'> & { password?: string }
) {
    const response = await apiFetch('/users', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
    })
    return await response.json()
}
