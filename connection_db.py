{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 128,
   "id": "07461bf8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import mysql.connector\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "id": "3f427a84",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Connection established successfully.\n",
      "Cursor created successfully.\n"
     ]
    }
   ],
   "source": [
    "\n",
    "try:\n",
    "    cnx = mysql.connector.connect(\n",
    "        host='127.0.0.1',\n",
    "        user='root',\n",
    "        password='',\n",
    "        database='py_connection'\n",
    "    )\n",
    "    print(\"Connection established successfully.\")\n",
    "\n",
    "    try:\n",
    "        cursor = cnx.cursor()\n",
    "        print(\"Cursor created successfully.\")\n",
    "        \n",
    "    except mysql.connector.Error as err:\n",
    "        print(\"Error creating cursor:\", err)\n",
    "\n",
    "\n",
    "except mysql.connector.Error as err:\n",
    "    print(\"Error during connection:\", err)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "id": "17efc098",
   "metadata": {},
   "outputs": [],
   "source": [
    "cursor.execute('SELECT * FROM `user`')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "1415f2d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'list'>\n",
      "hamza khouzima\n"
     ]
    }
   ],
   "source": [
    "rows = cursor.fetchall()\n",
    "print(type(rows))\n",
    "for row in rows:\n",
    "   print(row[1])\n",
    "\n",
    "cursor.close()\n",
    "cnx.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "id": "cde78380",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "print('')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f339d9e1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ccefd8aa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "43278b6d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "94f8f498",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00480b32",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b4b6978e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "704bcc27",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68ef0dc8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fce62f07",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "254a04fe",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
