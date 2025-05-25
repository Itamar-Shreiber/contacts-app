<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <form @submit.prevent="handleSubmit" class="contact-form">
        <h2>{{ contact?.id ? 'ערוך איש קשר' : 'הוסף איש קשר' }}</h2>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>

        <label for="first_name">שם פרטי:</label>
        <input id="first_name" v-model="form.first_name" required />

        <label for="last_name">שם משפחה:</label>
        <input id="last_name" v-model="form.last_name" required />

        <label for="email">אימייל:</label>
        <input id="email" type="email" v-model="form.email" required />

        <label for="phone">טלפון:</label>
        <input id="phone" type="tel" v-model="form.phone" required />

        <div class="buttons">
          <button type="submit" class="btn save">שמור</button>
          <button type="button" class="btn cancel" @click="$emit('close')">ביטול</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import { addContact, updateContact } from '../services/contactsApi.js'

export default {
  props: ['contact'],
  data() {
  return {
    form: {
      first_name: '',
      last_name: '',
      email: '',
      phone: ''
    },
    errorMessage: '' // נוסיף משתנה לשגיאה
  }
},
  watch: {
    contact: {
      immediate: true,
      handler(newVal) {
        this.form = newVal ? { ...newVal } : { first_name: '', last_name: '', email: '', phone: '' };
      }
    }
  },
  methods: {
  async handleSubmit() {
    this.errorMessage = ''; // איפוס שגיאה קודמת
    try {
      if (this.contact?.id) {
        await updateContact(this.contact.id, this.form);
      } else {
        await addContact(this.form);
      }
      this.$emit('saved');
    } catch (error) {
      if (error.response && error.response.data && error.response.data.message) {
        this.errorMessage = error.response.data.message;
      } else {
        this.errorMessage = 'אירעה שגיאה בלתי צפויה';
      }
    }
  }
}
}
</script>
