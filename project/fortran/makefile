
FC = gfortran

OBJECTS = 	euler.F90 \
			main.F90

EXE_FILE = euler

########################################################################################
#
#           COMPILING AND LINKING USING GENERIC SUFFIX RULE FOR f90
#
########################################################################################
$(EXE_FILE) : $(OBJECTS)
	@$(FC) $(OBJECTS) -o $(EXE_FILE)

#LET'S APPLY GENERIC SUFFIX RULE HERE FOR FORTRAN 90
%.o: %.F90
	$(FC) -c $<
	
#######################################################################################
#
#                            SOME USEFUL COMMANDS
#
#######################################################################################
clean:
	@rm -f *.o *.mod 
