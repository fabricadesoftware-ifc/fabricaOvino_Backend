<template>
  <section>
    <b-tabs vertical>
      <b-tab-item label="Ovelhas" icon="sheep">
        <!--<b-field grouped group-multiline>
          <div v-for="(column, index) in columns" :key="index">
            <b-checkbox v-model="column.visible">
              {{ column.label }}
            </b-checkbox>
          </div>
        </b-field> -->
        <b-table
          checkable
          :checked-rows.sync="checkedRows"
          striped
          :data="listSheeps"
          paginated
          paginate-position="bottom"
          aria-next-label="Next page"
          aria-previous-label="Previous page"
          aria-page-label="Page"
          aria-current-label="Current page"
          per-page="10"
        >
          <template v-slot="props">
            <b-table-column
              v-for="(column, index) in columns"
              :key="index"
              :field="column.field"
              sortable
              :label="column.label"
              :visible="column.visible"
              v-bind="column"
            >
              <template v-if="column.searchable" #searchable="props">
                <b-input
                  v-model="props.filters[props.column.field]"
                  placeholder="Pesquise..."
                  icon="magnify"
                />
              </template>
              <span v-if="column.field == 'birthday'">
                {{ new Date(props.row[column.field]).toLocaleDateString() }}
                <!-- -
                {{ new Date(props.row[column.field]).toLocaleTimeString() }} -->
              </span>
              <span v-if="column.field == 'sex'">
                <b-icon
                  :icon="
                    props.row[column.field] === 'Male'
                      ? 'gender-male'
                      : 'gender-female'
                  "
                >
                </b-icon>
                {{ props.row[column.field] }}
              </span>
              <span v-else>
                {{ props.row[column.field] }}
              </span>
            </b-table-column>
          </template>
          <template #bottom-left>
            <div class="buttons">
              <b-button
                type="is-primary"
                icon-left="plus-circle-outline"
                @click="save(checkedRows)"
                >{{ $t('buttons.add') }}</b-button
              >
              <b-button
                type="is-danger"
                icon-left="close-circle-outline"
                @click="checkedRows = []"
              >
                {{ $t('buttons.reset') }}
              </b-button>
            </div>
          </template>
        </b-table>
      </b-tab-item>
    </b-tabs>
    {{ checkedRows }}
  </section>
</template>

<script>
import { mapActions, mapState, mapGetters } from 'vuex'
//import { showError } from '@/plugins/global'
export default {
  data() {
    return {
      columns: [
        {
          field: 'earringNumber',
          label: this.$t('pages.admin.sheep.table.earringNumber'),
          searchable: true
          //visible: true
        },
        {
          field: 'breed',
          label: this.$t('pages.admin.sheep.table.breed'),
          searchable: true
          //visible: false
        },
        {
          field: 'category',
          label: this.$t('pages.admin.sheep.table.category'),
          searchable: true
          //visible: false
        },
        {
          field: 'lots',
          label: this.$t('pages.admin.sheep.table.lots'),
          searchable: true
          //visible: false
        },
        {
          field: 'sex',
          label: this.$t('pages.admin.sheep.table.sex'),
          searchable: true
          //visible: false
        },
        {
          field: 'birthday',
          label: this.$t('pages.admin.sheep.table.birthday'),
          searchable: true
          //visible: false
        }
      ],
      checkedRows: []
    }
  },
  computed: {
    ...mapGetters('sheeps', ['listSheeps']),
    ...mapState('lots', ['lots'])
  },
  created() {
    this.getSheeps()
  },
  methods: {
    ...mapActions('sheeps', ['getSheeps']),
    async save(checkedRows) {
      {
        alert(checkedRows)
      }
    }
  }
}
</script>

<style></style>
