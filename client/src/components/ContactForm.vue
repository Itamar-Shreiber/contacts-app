<template>
  <div class="modal-overlay" @click.self="$emit('close')">
    <div class="modal-content">
      <form @submit.prevent="handleSubmit" class="contact-form">
        <h2>{{ contact?.id ? 'ערוך איש קשר' : 'הוסף איש קשר' }}</h2>

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
      }
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
      if (this.contact?.id) {
        await updateContact(this.contact.id, this.form);
      } else {
        await addContact(this.form);
      }
      this.$emit('saved');
    }
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  direction: rtl;
}

.modal-content {
  background: white;
  padding: 30px 40px;
  border-radius: 10px;
  max-width: 400px;
  width: 90%;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  font-family: 'Arial', sans-serif;
}

.contact-form h2 {
  text-align: center;
  margin-bottom: 20px;
  color: #4caf50;
}

.contact-form label {
  display: block;
  margin: 10px 0 5px;
  font-weight: bold;
  color: #333;
}

.contact-form input {
  width: 100%;
  padding: 10px;
  border: 1px solid #bbb;
  border-radius: 5px;
  font-size: 16px;
  box-sizing: border-box;
  transition: border-color 0.3s;
}

.contact-form input:focus {
  outline: none;
  border-color: #4caf50;
}

.buttons {
  margin-top: 25px;
  display: flex;
  justify-content: space-between;
}

.btn {
  padding: 10px 25px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  color: white;
  transition: background-color 0.3s ease;
}

.btn.save {
  background-color: #4caf50;
}

.btn.save:hover {
  background-color: #388e3c;
}

.btn.cancel {
  background-color: #aaa;
}

.btn.cancel:hover {
  background-color: #777;
}
</style>
