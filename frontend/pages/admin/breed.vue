<template>
  <div class="breed-admin">
    <PageTitle
      icon="puzzle"
      :main="$t('pages.admin.breed.title')"
      :sub="$t('pages.admin.breed.subtitle')"
    />
    <div class="form">
      <input type="hidden" id="breed-id" v-model="breed.id" />
      <b-field
        :label="$t('pages.admin.forms.name.label')"
        class="breed-form-fields"
      >
        <b-input
          :placeholder="$t('pages.admin.forms.name.placeholder')"
          type="text"
          icon="tag"
          v-model="breed.name"
          :readonly="mode === 'remove'"
          required
        />
      </b-field>
      <div class="breed-form-buttons">
        <b-button
          v-if="mode === 'save'"
          type="is-info"
          icon-left="check"
          @click="save"
          >{{ $t('buttons.save') }}</b-button
        >
        <b-button
          v-else
          type="is-danger"
          icon-left="trash-can-outline"
          @click="remove"
          >{{ $t('buttons.delete') }}</b-button
        >
        <b-button type="is-dark" icon-left="redo" @click="reset">{{
          $t('buttons.reset')
        }}</b-button>
      </div>
    </div>
    <hr />
    <b-table
      striped
      :data="breeds"
      paginated
      paginate-position="bottom"
      aria-next-label="Next page"
      aria-previous-label="Previous page"
      aria-page-label="Page"
      aria-current-label="Current page"
      per-page="10"
    >
      <template slot-scope="props">
        <b-table-column
          v-for="(column, index) in columns"
          :key="index"
          :field="column.field"
          :sortable="column.sortable"
          :label="column.label"
          >{{ props.row[column.field] }}</b-table-column
        >

        <b-table-column
          field="actions"
          :label="$t('pages.admin.breed.table.actions')"
        >
          <b-button
            type="is-warning"
            icon-left="pencil"
            @click="loadBreed(props.row)"
          ></b-button>
          <b-button
            type="is-danger"
            icon-left="trash-can-outline"
            @click="loadBreed(props.row, 'remove')"
          ></b-button>
        </b-table-column>
      </template>
    </b-table>
  </div>
</template>

<script>
import PageTitle from '@/components/templates/PageTitle'
import { mapActions } from 'vuex'

import { showError } from '@/plugins/global'
export default {
  auth: false,
  components: { PageTitle },
  data: function () {
    return {
      mode: 'save',
      breed: {},
      breeds: [],
      columns: [
        {
          field: 'id',
          label: this.$t('pages.admin.breed.table.id'),
          sortable: true
        },
        {
          field: 'name',
          label: this.$t('pages.admin.breed.table.name'),
          sortable: true
        }
      ]
    }
  },
  async fetch() {
    this.breeds = await this.$axios.$get('/api/v1/breeds/')
  },
  methods: {
    ...mapActions('breeds', ['getBreeds']),
    loadBreed(breed, mode = 'save') {
      this.mode = mode
      this.breed = {
        id: breed.id,
        name: breed.name
      }
    },
    reset() {
      this.breed = {}
      this.path = ''
      this.mode = 'save'
      this.$fetch()
    },
    save() {
      const method = this.breed.id ? 'put' : 'post'
      const id = this.breed.id ? `/${this.breed.id}` : ''
      const url = `/api/v1/breeds${id}/`
      this.$axios[method](url, this.breed)
        .then(res => {
          this.$toasted.global.defaultSuccess()
          this.getBreeds()
          this.reset()
        })
        .catch(e => {
          for (var item in e.response.data) {
            this.$toast.error(item + ': ' + e.response.data[item])
          }
        })
    },
    remove() {
      const id = this.breed.id
      const url = `/api/v1/breeds/${id}`
      this.$axios
        .delete(url)
        .then(() => {
          this.$toasted.global.defaultSuccess()
          this.getBreeds()
          this.reset()
        })
        .catch(e => {
          for (var item in e.response.data) {
            this.$toast.error(item + ': ' + e.response.data[item])
          }
        })
    }
  }
}
</script>

<style></style>
