<template>
  <form @submit.prevent="submit">
    <input id="breed-id" v-model="breed.id" type="hidden" />
    <b-field
      :label="$t('pages.admin.forms.name.label')"
      message="Nome da raça"
      horizontal
    >
      <b-input
        v-model="breed.name"
        :placeholder="$t('pages.admin.forms.name.placeholder')"
        type="text"
        icon="tag"
        required
      />
    </b-field>
    <b-field horizontal>
      <b-field grouped>
        <div class="control">
          <b-button native-type="submit" type="is-primary">{{
            $t('buttons.save')
          }}</b-button>
        </div>
        <div class="control">
          <b-button type="is-primary is-outlined" @click="reset">{{
            $t('buttons.reset')
          }}</b-button>
        </div>
      </b-field>
    </b-field>
  </form>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  props: {
    value: {
      type: Object,
      default() {
        return {}
      }
    }
  },
  data() {
    return {
      original: {},
      breed: {}
    }
  },
  watch: {
    value(newValue) {
      this.original = { ...newValue }
      this.breed = newValue
    },
    breed(newValue) {
      this.$emit('input', newValue)
    }
  },
  created() {
    if (this.value) {
      this.original = { ...this.value }
      this.breed = this.value
    }
  },
  methods: {
    ...mapActions('breeds', ['getBreeds']),
    async submit() {
      try {
        const method = this.value.id ? 'put' : 'post'
        const id = this.value.id ? `/${this.value.id}` : ''
        const url = `/api/v1/breeds${id}/`
        await this.$axios[method](url, this.value)
        this.$toasted.global.defaultSuccess()
        this.getBreeds()
        this.reset('reload')
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.data[item])
        }
      }
    },
    reset(mode) {
      this.breed = this.breed.id && mode != 'reload' ? this.original : {}
    }
  }
}
</script>

<style></style>
