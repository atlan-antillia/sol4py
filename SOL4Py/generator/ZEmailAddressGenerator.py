#/******************************************************************************
# 
#  Copyright (c) 2020 Antillia.com TOSHIYUKI ARAI. ALL RIGHTS RESERVED.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#******************************************************************************/

# encoding: utf-8

# 2020/01/30

# This is NOT using yield.

import sys
import secrets
import numpy as np
import string

sys.path.append('../')

from SOL4Py.generator.ZGenerator import ZGenerator


###
#---------------------------------------------------------  
class ZEmailAddressGenerator(ZGenerator):
  ##
  # Constructor
  def __init__(self):
    pass


  def generate(self):
    alpabet = string.ascii_lowercase
    letters = string.ascii_lowercase + string.digits
    
    fname   = ''.join(secrets.choice(letters) for i in range(8) )
    
    sname   = ''.join(secrets.choice(letters) for i in range(6) )
    
    company = ''.join(secrets.choice(alpabet) for i in range(8) )
    
    domains = ["com", "net","org", "biz", "info", "gov", "us", "jp", "fr", "uk", "ca"]
    
    dindex = np.random.randint(0, len(domains)) 
    domain = domains[dindex]
    email =  fname + "." + sname + "@" + company + "." + domain
    return email


