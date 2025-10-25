class AgeDistribution:
    """Calculate and display age distribution"""
    
    @staticmethod
    def calculate_distribution(ages):
        """Calculate age distribution in groups"""
        if not ages:
            return {}
        
        total = len(ages)
        
        groups = {
            '< 20': 0,
            '20 to 40': 0,
            '40 to 60': 0,
            '> 60': 0
        }
        
        for age in ages:
            if age < 20:
                groups['< 20'] += 1
            elif 20 <= age <= 40:
                groups['20 to 40'] += 1
            elif 40 < age <= 60:
                groups['40 to 60'] += 1
            else:
                groups['> 60'] += 1
        
        # Calculate percentages
        distribution = {}
        for group, count in groups.items():
            percentage = (count / total) * 100
            distribution[group] = round(percentage, 2)
        
        return distribution
    
    @staticmethod
    def print_report(distribution):
        """Print age distribution report"""
        print("\n" + "="*50)
        print("📊 AGE DISTRIBUTION REPORT")
        print("="*50)
        print(f"{'Age-Group':<15} {'% Distribution':>15}")
        print("-"*50)
        
        for group, percentage in distribution.items():
            print(f"{group:<15} {percentage:>14.2f}%")
        
        print("="*50 + "\n")