# ====================== BEGIN GPL LICENSE BLOCK ============================
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	 See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.	 If not, see <http://www.gnu.org/licenses/>.
#  All rights reserved.
#
# ======================= END GPL LICENSE BLOCK =============================

# ----------------------------------------------
#  BPS -> BleuRaven Python Script
#  BleuRaven.fr
#  XavierLoux.com
# ----------------------------------------------

import time


class CounterTimer():
    """
    A simple timer.
    """

    def __init__(self):
        self.start = time.perf_counter()

    def reset_time(self):
        """
        Reset the timer.
        """
        self.start = time.perf_counter()

    def get_time(self):
        """
        Get the elapsed time since the timer started. (Class create)
        """
        return time.perf_counter() - self.start
        
    def get_str_time(self):
        """
        Get the elapsed str time since the timer started. (Class create)
        """
        elapsed_time = self.get_time()
        if elapsed_time < 60:
            return f"{elapsed_time:.2f} secondes"
        elif elapsed_time < 3600:
            minutes, seconds = divmod(elapsed_time, 60)
            return f"{int(minutes)} minutes et {seconds:.2f} secondes"
        else:
            hours, remainder = divmod(elapsed_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{int(hours)} heures, {int(minutes)} minutes et {seconds:.2f} secondes"

