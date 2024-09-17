class Action:
    def __init__(self, anio, mes, horaSolicitud, horaIntervencion, cod, distrito, hospital):
        self._anio = anio
        self._mes = mes
        self._horaSolicitud = horaSolicitud
        self._horaIntervencion = horaIntervencion
        self._cod = cod
        self._distrito = distrito
        self._hospital = hospital

    def getAnio(self):
        return self._anio

    def getMes(self):
        return self._mes

    def getHoraSolicitud(self):
        return self._horaSolicitud

    def getHoraIntervencion(self):
        return self._horaIntervencion

    def getCod(self):
        return self._cod

    def getDistrito(self):
        return self._distrito

    def getHospital(self):
        return self._hospital

    def setAnio(self, anio):
        self._anio = anio

    def setMes(self, mes):
        self._mes = mes

    def setHoraSolicitud(self, horaSolicitud):
        self._horaSolicitud = horaSolicitud

    def setHoraIntervencion(self, horaIntervencion):
        self._horaIntervencion = horaIntervencion

    def setCod(self, cod):
        self._cod = cod

    def setDistrito(self, distrito):
        self._distrito = distrito

    def setHospital(self, hospital):
        self._hospital = hospital
