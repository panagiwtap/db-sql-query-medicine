import sys
import MySQLdb
from MySQLdb.cursors import SSCursor

def connectDB():
    return MySQLdb.connect("dummyserver", "dummyusername", "dummypassword", "dummydatabasename")


if __name__ == "__main__":
    conn = connectDB()
    if (conn != -1):
        print("Connection with the Database has been enstablished!")

        conn.begin()
        cursor = conn.cursor()
		# ftiakse to mysql query me thn eisodo tou kwdikou astheneias
        query= """
        SELECT `systatiko`.`onoma`
        FROM `systatiko`
        JOIN `proteinh_systatiko` ON `proteinh_systatiko`.`systatiko` = `systatiko`.`onoma`
        JOIN `proteinh` ON `proteinh`.`proteinh_id` = `proteinh_systatiko`.`proteinh`
        JOIN `gonidio_proteinh` ON `gonidio_proteinh`.`proteinh` = `proteinh`.`proteinh_id`
        JOIN `gonidio` ON `gonidio_proteinh`.`gonidio` =`gonidio`.`symbolo`
        JOIN `asthenia_gonidio` ON `asthenia_gonidio`.`gonidio` = `gonidio`.`symbolo`
        JOIN `asthenia` ON `asthenia`.`asthenia_id` = `asthenia_gonidio`.`asthenia`
        WHERE `asthenia`.`asthenia_id` = '%s'
		"""  % (sys.argv[1]);
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            print "Ingredients related to disease id " + str(sys.argv[1])
            print "=========================================="
            for row in results:
                # emfanise thn prwth sthlh tou apotelesmatos tou query
                print (row[0]);
        except:
            print("Error: unable to fecth data")
        conn.commit()
        cursor.close()
        conn.close()
    else:
        print("There was a problem with the Database connection..")
		
	